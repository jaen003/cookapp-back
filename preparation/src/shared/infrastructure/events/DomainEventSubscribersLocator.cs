/* 
 * 
 * Libraries
 *
*/

using System.Reflection;
using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class DomainEventSubscribersLocator { 

        /* 
         * 
         * Methods
         *
        */

        public static List<Type> locate( Type eventClass ) {
            // Variables
            List<Type>            subscriberClasses;
            Assembly              assembly;    
            IEnumerable<TypeInfo> satisfiedClasses;
            IEnumerable<TypeInfo> classTypes;
            IEnumerable<TypeInfo> implementedInterfaces;
            // Code
            assembly   = Assembly.Load( "preparation" );
            classTypes = assembly.GetExportedTypes().Select(
                i => i.GetTypeInfo()
            ).Where( i => i.IsClass && !i.IsAbstract );
            subscriberClasses = new List<Type>();
            foreach( TypeInfo classType in classTypes ) {
                implementedInterfaces = classType.ImplementedInterfaces.Select( i => i.GetTypeInfo() );
                satisfiedClasses = implementedInterfaces.Where( i =>
                    i.IsGenericType && 
                    i.GetGenericTypeDefinition() == typeof( DomainEventSubscriber<> ) &&
                    i.GenericTypeArguments.FirstOrDefault() == eventClass
                );
                if( satisfiedClasses.Count() != 0 ) {
                    subscriberClasses.Add( classType.AsType() );
                }
            }
            return subscriberClasses;
        }
    
    }

}