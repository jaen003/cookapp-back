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

    public class DomainEventsLocator { 

        /* 
         * 
         * Methods
         *
        */

        public static List<Type> locate() {
            // Variables
            List<Type>            eventClasses;
            Assembly              assembly;    
            IEnumerable<TypeInfo> satisfiedClasses;
            IEnumerable<TypeInfo> classTypes;
            // Code
            assembly   = Assembly.Load( "preparation" );
            classTypes = assembly.ExportedTypes.Select(
                i => i.GetTypeInfo()
            ).Where( i => i.IsClass && !i.IsAbstract );
            satisfiedClasses = classTypes.Where( i => i.IsSubclassOf( typeof( DomainEvent ) ) );
            eventClasses     = new List<Type>();
            eventClasses.AddRange( satisfiedClasses.Select( i => i.AsType() ) );
            return eventClasses;
        }
    
    }

}